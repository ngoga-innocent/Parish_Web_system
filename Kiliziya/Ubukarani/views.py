from django.shortcuts import render, redirect
from .bapteme import RawKwiyandikisha
from .models import Icyangombwa, Ibyasabwe
from django.contrib import messages


# generating pdf files import
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

# Create your views here.


def Home(request):
    return render(request, 'Ubukarani.html')


def Register(request):

    form = RawKwiyandikisha()
    if request.method == "POST":
        form = RawKwiyandikisha(request.POST)
        if form.is_valid():
            Icyangombwa.objects.create(**form.cleaned_data)
            redirect('/')

            # form = Kwiyandikisha(request.POST or None)
            # if form.is_valid():
            #     form.save()
    context = {'form': form}
    return render(request, 'icyangombwa.html', context)


def icyemezo(request):
    if request.method == "POST":
        searched = request.POST['search']
        searchup = searched.capitalize()
        icyangombwa = Icyangombwa.objects.filter(
            prenom__contains=searchup)
        if icyangombwa:
            for icyango in icyangombwa:
                icyasabwe = Ibyasabwe.objects.filter(owner_id=icyango.id)
                if icyasabwe:
                    for icya in icyasabwe:
                        status = icya.status
                        if status == 1:
                            status = "Pending"
                        else:
                            status = 'Approved'
                        context = {
                            'status': status,
                            'searched': searched,
                            'icyangombwa': icyangombwa
                        }
                    return render(request, 'ibyangombwa.html', context)
                else:
                    context = {
                        'searched': searched,
                        'icyangombwa': icyangombwa
                    }
                    return render(request, 'ibyangombwa.html', context)
        else:
            messages.info(request, "Ifishi yawe ntiri muri system")
            return render(request, 'ibyangombwa.html')
    else:
        return render(request, 'ibyangombwa.html')


def icyemezo_detail(request, id):
    if request.method == "POST":
        amazina = request.POST['amazina']

        umuryangoremezo = request.FILES['umuryangoremezo']
        batisimu = request.FILES['batisimu']
        owner_id = request.POST['id']
        ibyasabwe = Ibyasabwe.objects.create(
            amazina=amazina, umubyeyi=batisimu, umuryangoremezo=umuryangoremezo, status=1, owner_id=owner_id)
        ibyasabwe.save()
        return redirect('/ubukarani/icyemezo')
    else:
        icyemezo = Icyangombwa.objects.get(id=id)
        id = icyemezo.id
        nom = icyemezo.Nom
        prenom = icyemezo.prenom
        context = {
            'id': id,
            'icyemezo': icyemezo,
            'nom': nom,
            'prenom': prenom
        }
        return render(request, 'icyangombwacyawe.html', context)


def Generatepdf(request, id):
    ifishi = Icyangombwa.objects.get(id=id)

    template = get_template('downlodable.html')
    data = {

        'amazina': ifishi.prenom,
        'nom': ifishi.Nom,
        'papa': ifishi.papa,
        'mama': ifishi.mama,
        'umubyeyi': ifishi.umubyeyi_wa_batisimu,
        'parroise': ifishi.parroise,
        'province': ifishi.province,
        'district': ifishi.District,
        'amavuko': ifishi.itariki_yamavuko,
        'batisimu': ifishi.batisimu,
        'ukaristiya': ifishi.Ukaristiya,
        'gukomezwa': ifishi.Gukomezwa
    }
    html = template.render(data)

    pdf = render_to_pdf('downlodable.html', data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Ifishi_%s.pdf" % (ifishi.prenom)
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        return response

        # if download:
        #     content = "attachment; filename='%s'" % (filename)
        #     response['Content-Disposition'] = content
        # return HttpResponse("Not found")
    # return HttpResponse(pdf, content_type='application/pdf')

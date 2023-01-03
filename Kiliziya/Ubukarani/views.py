from django.shortcuts import render, redirect
from .bapteme import RawKwiyandikisha
from .models import Icyangombwa


# generating pdf files import
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

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
        icyangombwa = Icyangombwa.objects.filter(amazina__contains=searched)
        context = {
            'searched': searched,
            'icyangombwa': icyangombwa
        }
        return render(request, 'ibyangombwa.html', context)
    else:
        return render(request, 'ibyangombwa.html')


def icyemezo_detail(request, id):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    icyemezo = Icyangombwa.objects.get(id=id)
    lines = []
    lines.append(icyemezo.amazina)
    lines.append(icyemezo.papa)
    lines.append(icyemezo.mama)
    lines.append(icyemezo.umubyeyi_wa_batisimu)
    lines.append(icyemezo.parroise)
    # lines.append(icyemezo.batisimu)
    # lines.append(icyemezo.Ukaristiya)
    # lines.append(icyemezo.Gukomezwa)

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # return FileResponse(buf, as_attachment=True, filename='icyangombwa.pdf')
    context = {
        'icyemezo': icyemezo
    }
    return render(request, 'icyangombwacyawe.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm  # Assuming you have created a form for image upload
from PIL import Image

def ascii_convert(image_file):
    scale = 3  # Default scale
    img = Image.open(image_file)
    w, h = img.size
    img.resize((w // scale, h // scale)).save("resized.jpg")
    img = Image.open("resized.jpg")
    w, h = img.size
    grid = [["X"] * w for _ in range(h)]
    pix = img.load()
    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pix[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pix[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pix[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pix[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pix[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pix[x,y]) in range(700,750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
    with open("output.txt", "w") as art:
        for row in grid:
            art.write("".join(row) + "\n")
    return "output.txt"

def convert_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            ascii_file = ascii_convert(uploaded_file)
            with open(ascii_file, 'r') as f:
                response = HttpResponse(f.read(), content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename="output.txt"'
            return response
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

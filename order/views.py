from django.shortcuts import render,redirect
from .models import Order
from .forms import OrderForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from order.models import Order
from io import BytesIO 


# Create your views here.
def get_orders(request):
    orders = Order.objects.all()
    order_count = Order.objects.count()
    context = {"orders":orders,"order_count":order_count}
    return render(request,"order/orders.html",context)


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_orders')  # Redirect to a page showing the list of orders or any other page you prefer
    else:
        form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})

def get_receipts(request):
    pass

def generate_receipt(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Set up styles
    p.setFont("Helvetica-Bold", 16)
    leading = 20  # Line spacing

    # Header
    p.drawString(100, height - 80, "Receipt for Order")
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, "-" * 60)
    p.drawString(100, height - 120, f"Order Number: {order.order_number}")
    p.drawString(100, height - 140, f"Order Date: {order.order_date}")
    p.drawString(100, height - 160, f"Supplier: {order.supplier.name}")
    p.drawString(100, height - 180, "-" * 60)

    # Products section
    y_position = height - 220
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y_position, "Products:")
    p.setFont("Helvetica", 12)
    y_position -= leading

    for product in order.products.all():
        p.drawString(100, y_position, f"Name: {product.name}")
        y_position -= leading
        p.drawString(100, y_position, f"Quantity: {product.quantity}")
        y_position -= leading
        p.drawString(100, y_position, f"Code: {product.product_code}")
        y_position -= leading
        p.drawString(100, y_position, f"Price: R {product.price:.2f}")
        y_position -= leading
        p.drawString(100, y_position, "-" * 60)
        y_position -= leading * 2

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

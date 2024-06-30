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

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Receipt for Order: {order.order_number}")
    p.drawString(100, height - 120, f"Date: {order.order_date}")
    p.drawString(100, height - 140, f"Supplier: {order.supplier.name}")

    y_position = height - 180
    for product in order.products.all():
        p.drawString(100, y_position, f"Product: {product.name} - Quantity: {product.quantity}")
        y_position -= 20

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

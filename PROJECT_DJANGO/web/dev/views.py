from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .models import *
from django.template import loader
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.contrib.sessions.models import Session
def index(request):  
    return user_home(request)
def adminlogout(request):
    del request.session['USERNAME']
    return render(request,"dev/adminlogin.html")
def admin_logpage(request):
    return render(request,'dev/adminlogin.html')
def logadmin(request):
    template = loader.get_template("dev/adminlogin.html")
    context = {}
    if request.method == 'POST':
        try:
            adminName = request.POST['adminuser']
            adminPass = request.POST['adminpass']
            login_obj = Adminlogin.objects.filter(Username=adminName).exists()
            if login_obj:
                admin_obj = Adminlogin.objects.get(Username=adminName,Password=adminPass)
                request.session['USERNAME'] = admin_obj.Username
                #return adminhome(request)
                allproduct = Product.objects.all()
                context = {'Product':allproduct}
                template = loader.get_template("dev/adminhome.html")
            else:
                context = {'error':'Invalid Admin'}
                HttpResponse(template.render(context,request))
        except Exception as e:
            context = {'error': e }
            HttpResponse(template.render(context,request))
    return HttpResponse(template.render(context,request))
def addproduct(request):
    return render(request,"dev/addproduct.html",{'msg':''})
def adminhome(request):
    allproduct = Product.objects.all()
    return render(request,"dev/adminhome.html",{'Product':allproduct})
def upload_product(request):
    if request.method == 'POST':
        Pname = request.POST['pname']
        Pcolor = request.POST['pcolor']
        Pbrand = request.POST['pbrand']
        Psize = request.POST['psize']
        Pprice = request.POST['pprice']
        Pfile = request.FILES['pfile']
        fs = FileSystemStorage()
        filename = Pfile.name
        fs.save(filename, Pfile)
        file_upload = Product(Product_name=Pname,Product_color=Pcolor,Product_brand=Pbrand,Product_size=Psize,Product_price=Pprice,Product_photo=filename)
        file_upload.save()
        return render(request,"dev/addproduct.html",{'msg':'Uploaded Successfully'})
    return render(request,"dev/addproduct.html")
def delete_pro(request, id):
    product = Product.objects.get(id=id)
    fs = FileSystemStorage()
    if FileSystemStorage.exists(fs,product.Product_photo):
        FileSystemStorage.delete(fs,product.Product_photo)
        product.delete()
    return adminhome(request)
def edit_pro(request, id):
    product = Product.objects.get(id=id)
    return render(request,"dev/editproduct.html",{'product':product})
def upload_pro(request, id):
    try:
        products = Product.objects.get(id=id)
        products.Product_name = request.POST['pname']
        products.Product_color = request.POST['pcolor']
        products.Product_brand = request.POST['pbrand']
        products.Product_size = request.POST['psize']
        products.Product_price = request.POST['pprice']
        if 'pfile' in request.FILES:
            myFile = request.FILES['pfile']
            fs = FileSystemStorage()
            FileSystemStorage.delete(fs,products.Product_photo)
            file_name = myFile.name
            fs.save(file_name,myFile)
            products.Product_photo = file_name
            products.save()
        else:
            products.save()
    except Exception as e:
        context = {'error': e}
        return render(request,"dev/editproduct.html",context)
    return adminhome(request)


def purchase(request):
    allpro=Product.objects.all()
    return render(request,"dev/purchase.html",{'product':allpro,'msg':''})
def uploadpur(request):
    if request.method == 'POST':
        purid = request.POST['productid']
        purqnty = request.POST['pur_qnty']
        purprice = request.POST['pur_price']
        puramt = request.POST['pur_amt']
        purchaseupload = Purchase(Product_id=purid,Pur_date=datetime.now(),Pur_quantity=purqnty,Pur_price=purprice,Pur_amount=puramt)
        purchaseupload.save()
        stock_obj = Stock.objects.filter(Product_id=purid).exists()
        if stock_obj:
            stocks = Stock.objects.get(Product_id=purid)
            qty=stocks.P_quantity
            stocks.P_quantity=int(qty)+int(purqnty)
            stocks.save()
        else:
            stockupload = Stock(Product_id=purid,P_quantity=purqnty)
            stockupload.save()
        allproduct=Product.objects.all()
        return render(request,"dev/purchase.html",{'product':allproduct,'msg':'Purchased Successfully'})
    return adminhome(request)
    
def viewpur(request):
    allpur=Purchase.objects.raw('select dev_Purchase.id,dev_Purchase.Product_id,Pur_date,Pur_quantity,Pur_price,Pur_amount,Product_name from dev_Purchase inner join dev_Product on(dev_Purchase.Product_id=dev_Product.id)')
    return render(request,"dev/viewpurchase.html",{'itemss':allpur})

def del_purchase(request,id):
    allpro = Purchase.objects.get(id=id)
    allpro.delete()
    return viewpur(request)
def view_stockes(request):
    allstock=Stock.objects.raw('select dev_Stock.id,dev_Stock.Product_id,P_quantity,dev_Product.Product_name from dev_Stock inner join dev_Product on( dev_Stock.Product_id=dev_Product.id)')
    return render(request,"dev/stock.html",{'stock':allstock})
def editstock(request, id):
    stock = Stock.objects.get(id=id)
    return render(request,"dev/editstock.html",{'s':stock})
def update_stock(request, id):
    if request.method == 'POST':
        stock=Stock.objects.get(id=id)
        stock.P_quantity = request.POST['pqnty']
        stock.save()
        return view_stockes(request)
    return adminhome(request)
def userlist(request):
    alluser=Userlogin.objects.all()
    return render(request,"dev/userslist.html",{'user':alluser})
def removeUser(request, id):
    users = Userlogin.objects.get(id=id)
    user_name = users.Username
    users.delete()
    alluser=Userlogin.objects.all()
    return render(request,"dev/userslist.html",{'user':alluser,'userName':user_name,'msg':'Successfully Removed'})
def view_sales(request):
    allsale=Sales.objects.raw('select dev_Sales.id,dev_Sales.Product_id,Sale_quantity,Sale_amount,Product_name from dev_Sales inner join dev_product on(dev_Sales.Product_id=dev_Product.id)')
    return render(request,"dev/viewsales.html",{'saleitem':allsale})
def del_sale(request,id):
    s = Sales.objects.get(id=id)
    s.delete()
    return redirect("/view_sales")
def product_data(request, id):
    pro = Product.objects.get(id=id)
    context = {}
    Sobj = Stock.objects.filter(Product_id=id).exists()
    if Sobj:
        stocks = Stock.objects.get(Product_id=id)
        qnty = stocks.P_quantity
        if int(qnty) == 0:
            context = 'Out of stock'
        elif int(qnty) < 12:
            context = 'Only few stocks available'
        else:
            context ='In stock'
    else:
        context = 'Not available'
    return render(request,'dev/product_details.html',{'product':pro,'msg':context})

def user_home(request):
    allpro = Product.objects.all().order_by('id')[ : :-1 ]
    return render(request,"dev/index.html",{'product':allpro})
def login_page(request):
    return render(request,"dev/userlogin.html")
def reg(request):
    return render(request,"dev/registration.html")
def reg_user(request):
    if request.method == 'POST':
        Nuser = request.POST['txtuser']
        Npass = request.POST['txtpass']
        userobj = Userlogin.objects.filter(Username=Nuser).exists()
        if userobj:
            return render(request,'dev/registration.html',{'msg':'Username not available choose different Username'})
        else:
            newobj = Userlogin(Username=Nuser,Password=Npass)
            newobj.save()
            return login_page(request)
    return reg(request)
def usr(request):
    if request.method == 'POST':
        Nuser = request.POST['txtuser']
        Npass = request.POST['txtpass']
        Nobj = Userlogin.objects.filter(Username=Nuser,Password=Npass).exists()
        if Nobj:
            try:
                newobj = Userlogin.objects.get(Username=Nuser,Password=Npass)
                request.session['UNAME'] =newobj.Username
                allpro = Product.objects.all()
                return render(request,"dev/index.html",{'product':allpro})
            except Exception as e:
                return render(request,"dev/userlogin",{'msg':e})
        else:
            return render(request,"dev/userlogin.html",{'msg':'user not found'})
def ulogout(request):
    del request.session['UNAME']
    #Session.objects.all().delete()
    return user_home(request)
def buy(request, id):
    qnty = request.POST['txtqnty']
    pro_obj = Product.objects.get(id=id)
    price = pro_obj.Product_price
    total = int(qnty)*int(price)
    stock_obj = Stock.objects.filter(Product_id=id).exists()
    if stock_obj:
        s_obj = Stock.objects.get(Product_id=id)
        sqnty = s_obj.P_quantity
        s_obj.P_quantity = int(sqnty)-int(qnty)
        s_obj.save()
        sales = Sales(Product_id=id,Sale_quantity=qnty,Sale_amount=total)
        sales.save()
        return HttpResponse("<h1>Successfully Purchased</h1><br>Total Amount ="+str(total))
    else:
        return HttpResponse("<h1>Product Not Available</h1>")
def search(request):
    if request.method == 'POST':
        value = request.POST['searching']
        val='%s%%'%value # %adidas%
        allpro = Product.objects.raw("select * from dev_Product where Product_name or Product_brand like %s ",[val])
        return render(request,"dev/search.html",{'product':allpro})
    return redirect("/user_home")
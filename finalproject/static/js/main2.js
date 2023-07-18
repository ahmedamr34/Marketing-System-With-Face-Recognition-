var productCompanyInput = document.getElementById('productCompanyInput');
var productBrandInput =document.getElementById('productBrandInput');
var productNameInput = document.getElementById('productNameInput');//Input kolo
var productPriceInput = document.getElementById('productPriceInput');//Input kolo
var productCategoryInput = document.getElementById('productCategoryInput');//Input kolo
var productDescInput = document.getElementById('productDescInput');//Input kolo
var addBtn = document.getElementById("addBtn");
var currentIndex = 0;
var productsContainer=[] ;

if(localStorage.getItem('myProducts') != null)
{   
    productsContainer = JSON.parse( localStorage.getItem('myProducts') );
    displayProducts(productsContainer);
}
else
{
    productsContainer = [];
}
addBtn.onclick = function () {
    if (addBtn.innerHTML == 'add Product') {
        addProduct();
    } else {
        updateProducts();
    }
    displayBooks()
    reset();
}

function addProduct() {
    if(validateProductName()== true)
    {
        var product = {
            company:productCompanyInput.value,
            brand:productBrandInput.value,
            name: productNameInput.value,
            price: productPriceInput.value,
            category: productCategoryInput.value,
            desc: productDescInput.value
        }
        productsContainer.push(product);//1000
        localStorage.setItem('myProducts',JSON.stringify(productsContainer) )
        clearForm();
        displayProducts(productsContainer);
    }
    else {
        updateProducts();


    }   
}

function clearForm() {
    productCompanyInput.value = "";
    productBrandInput.value = "";
    productNameInput.value = "";
    productNameInput.classList.remove('is-valid')
    productPriceInput.value = "";
    productCategoryInput.value = "";
    productDescInput.value = "";

}
function displayProducts(list) {

    var cartoona = ``;
    for (var i = 0; i < list.length; i++) {
        cartoona += ` <tr>
        <td>${ list[i].company }</td>
        <td>${list[i].brand}</td>
        <td>${ list[i].name }</td>
        <td>${list[i].price}</td>
        <td>${list[i].category}</td>
        <td>${list[i].desc}</td>
        <td><button onclick="getProdcutsInfo(${i})"  class="btn btn-sm btn-warning">update</button> </td>
    </tr>`;
    }
    document.getElementById('tableBody').innerHTML = cartoona;
} 
function getProdcutsInfo(index) {
    currentIndex = index;
    var currentProdct = productsContainer[index];
    productCompanyInput.value = currentProdct.company;
    productBrandInput.value = currentProdct.brand;
    productNameInput.value = currentProdct.name;
    productPriceInput.value = currentProdct.price;
    productCategoryInput.value = currentProdct.category;
    productDescInput.value = currentProdct.desc;
    addBtn.innerHTML = "Update Product"
}


function updateProducts() {
    alert(currentIndex)
    var product = {
        company:productCompanyInput.value,
        brand:productBrandInput.value,
        name: productNameInput.value,
        price: productPriceInput.value,
        category: productCategoryInput.value,
        desc: productDescInput.value
    }
    productsContainer[currentIndex]=product;
    localStorage.setItem('myProducts',JSON.stringify(productsContainer) )
      
  }
  

// 
   
function validateProductName ()
{
    var regex =/^[A-Z][a-z]{3,6}$/;
    if(regex.test(productNameInput.value)== true)
    {
        productNameInput.classList.replace('is-invalid','is-valid')
        return true;

    }
    else{
        productNameInput.classList.add('is-invalid')
        return false;
    }


}




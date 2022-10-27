const title = document.getElementById("title");
const description = document.getElementById("description");
const brand = document.getElementById("brand");
const price = document.getElementById("price");
const csrf_token = document.getElementsByName("csrfmiddlewaretoken");
const form = document.getElementById("p-form");
const tBody = document.getElementById("t-body");
$.ajax({
  type: "GET",
  url: "/product/list/",
  success: function (response) {
    console.log(response.data);
    data = response.data;
    data.forEach((pd) => {
      tBody.innerHTML += `
                <tr id="product-${pd.id}">
                    <th scope="row">${pd.id}</th>
                    <td>${pd.title}</td>
                    <td>${pd.price}</td>
                    <td>${pd.brand}</td>
                    <td>
                    <button type="button" onclick="editProduct(${pd.id})" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#exampleModal">
                      Update
                    </button>
                    </td>
                </tr>
            `;
    });
  },
  error: function (error) {
    console.log(error);
  },
});
// TODO: CRUD OPERATION
$("#p-form").submit(function (e) {
  e.preventDefault();
  let titleValue = title.value;
  let descriptionValue = description.value;
  let brandValue = brand.value;
  let priceValue = price.value;

  if (titleValue === "") {
    return console.log("enter the title value");
  }
  if (descriptionValue === "") {
    return console.log("enter the description value");
  }
  if (brandValue === "") {
    return console.log("enter the brand value");
  }
  if (priceValue === "") {
    return console.log("enter the price value");
  }
  const productData = {
    csrfmiddlewaretoken: csrf_token[0].value,
    title: titleValue,
    description: descriptionValue,
    brand: brandValue,
    price: priceValue,
  };
  console.log(productData);
  $.ajax({
    url: "/products/create/",
    type: "POST",
    data: productData,
    success: function (data) {
      console.log(data);
    },
  });
  $("#p-form")[0].reset();
});

// Create Django Ajax Call
$("form#updateUser").submit(function () {
  var idInput = $('input[name="formId"]').val().trim();
  var nameInput = $('input[name="formName"]').val().trim();
  var addressInput = $('input[name="formAddress"]').val().trim();
  var ageInput = $('input[name="formAge"]').val().trim();
  if (nameInput && addressInput && ageInput) {
    // Create Ajax Call
    $.ajax({
      url: '{% url "crud_ajax_update" %}',
      data: {
        id: idInput,
        name: nameInput,
        address: addressInput,
        age: ageInput,
      },
      dataType: "json",
      success: function (data) {
        if (data.user) {
          updateToUserTabel(data.user);
        }
      },
    });
  } else {
    alert("All fields must have a valid value.");
  }
  $("form#updateUser").trigger("reset");
  $("#myModal").modal("hide");
  return false;
});

// Update Django Ajax Call
function editProduct(id) {
  if (id) {
    product_id = "#product-" + id;
    console.log(product_id);
    titleUpdate = $(product_id).find("#titleUpdate").text();
    console.log(titleUpdate);
    // title = $(product_id).find(".userName").text();
    // address = $(product_id).find(".userAddress").text();
    // age = $(product_id).find(".userAge").text();
    // $("#form-id").val(id);
    // $("#form-name").val(name);
    // $("#form-address").val(address);
    // $("#form-age").val(age);
  }
}

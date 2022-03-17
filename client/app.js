function getSalesCat() {
    var uiSale = document.getElementsByName("uiSale");
    for(var i in uiSale) {
      if(uiSale[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; 
  }

function getCommodity() {
    var uiCom = document.getElementsByName("uiCom");
    for(var i in uiCom) {
      if(uiCom[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; 
}
function onClickedEstimatePrice() {
    
    var com = getCommodity();
    var sales = getSalesCat();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatePrice");
  
    var url = "http://127.0.0.1:5000/predict_price";
  
    $.post(url, {
        commodity: com,
        sales_catagory: sales,
        location: location.value
    },function(data, status) {
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }

function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location"; 
    $.get(url,function(data, status) {
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }
  window.onload=onPageLoad;
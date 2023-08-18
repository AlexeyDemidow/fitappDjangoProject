$(document).ready(function () {
    $('select').selectize({
        sortField: 'text',
        maxItems: 1,
        placeholder: 'Нажмите чтобы выбрать продукт ...',
    });
})


//var config = {
//  type: 'bar',
//  data: {
//    datasets: [{
//      data: {{ data|safe }},
//      backgroundColor: [
//        '#696969', '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
//      ],
//      label: 'Calories'
//    }],
//    labels: {{ labels|safe }}
//  },
//  options: {
//    responsive: true
//  }
//};
//
//window.onload = function() {
//  var ctx = document.getElementById('chart').getContext('2d');
//  window.myPie = new Chart(ctx, config);
//};

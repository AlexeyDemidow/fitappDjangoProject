var br_config = {
              type: 'pie',
              data: {
                datasets: [{
                  data: $("#data_breakfast").text(),
                  backgroundColor: [
                    '#3d2e2e', '#514d4d', '#6b6666'
                  ],
                  label: 'Breakfast'
                }],
                labels: {{ food_nutrients_labels|safe }}
              },
              options: {
                responsive: true
              }
            };

            var lu_config = {
              type: 'pie',
              data: {
                datasets: [{
                  data: {{ data_lunch|safe }},
                  backgroundColor: [
                    '#3d2e2e', '#514d4d', '#6b6666'
                  ],
                  label: 'Lunch'
                }],
                labels: {{ food_nutrients_labels|safe }}
              },
              options: {
                responsive: true
              }
            };

            var di_config = {
              type: 'pie',
              data: {
                datasets: [{
                  data: {{ data_dinner|safe }},
                  backgroundColor: [
                    '#3d2e2e', '#514d4d', '#6b6666'
                  ],
                  label: 'Dinner'
                }],
                labels: {{ food_nutrients_labels|safe }}
              },
              options: {
                responsive: true
              }
            };

            var sn_config = {
              type: 'pie',
              data: {
                datasets: [{
                  data: {{ data_snacks|safe }},
                  backgroundColor: [
                    '#3d2e2e', '#514d4d', '#6b6666'
                  ],
                  label: 'Snacks'
                }],
                labels: {{ food_nutrients_labels|safe }}
              },
              options: {
                responsive: true
              }
            };

            var cal_config = {
              type: 'bar',
              data: {
                datasets: [{
                  data: {{ food_category_data|safe }},
                  backgroundColor: [
                    '#bababa', '#a1a1a1', '#878787', '#878787'
                  ],
                  label: 'Калории'
                }],
                labels: {{ food_category_labels|safe }}
              },
              options: {
                responsive: true,
                legend: {
                    display: false
                }
              }
            };

            window.onload = function() {
              var br = document.getElementById('chart_breakfast').getContext('2d');
              window.myPie = new Chart(br, br_config);

              var lu = document.getElementById('chart_lunch').getContext('2d');
              window.myPie = new Chart(lu, lu_config);

              var di = document.getElementById('chart_dinner').getContext('2d');
              window.myPie = new Chart(di, di_config);

              var sn = document.getElementById('chart_snacks').getContext('2d');
              window.myPie = new Chart(sn, sn_config);

              var cal = document.getElementById('chart_calories').getContext('2d');
              window.myPie = new Chart(cal, cal_config);
            };
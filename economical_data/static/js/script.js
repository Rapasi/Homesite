function fetchDataAndPopulate(url, tableId, chartId, graphLabel) {
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const jsonData = JSON.parse(data.data);
        const tableBody = document.getElementById(tableId).getElementsByTagName('tbody')[0];
        const timePeriods = [];
        const observationValues = [];
          
        
        let latestData = null;

        jsonData.forEach(row => {
            timePeriods.push(row.fields.TIME_PERIOD);
            observationValues.push(row.fields.OBS_VALUE);

            // Update the latestData based on TIME_PERIOD
            if (latestData === null || row.fields.TIME_PERIOD > latestData.fields.TIME_PERIOD) {
                latestData = row;
            }
        });

        // Add only the latest data to the table
        if (latestData) {
            const newRow = tableBody.insertRow();
            newRow.insertCell(0).innerText = latestData.fields.TIME_PERIOD;
            newRow.insertCell(1).innerText = latestData.fields.OBS_VALUE;
        } else {
            alert('No data available');
        }

        // Draw the graph
        const ctx = document.getElementById(chartId).getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timePeriods,
                datasets: [{
                    label: graphLabel,  // Use dynamic label
                    data: observationValues,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    fill: false
                }]
            },
            options: {
                scales: {
                  x: {
          
                        title: {
                            display: true,
                            text: 'Time Period'
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: graphLabel  // Use dynamic label for y-axis as well
                        }
                    }
                }
            }
        });
      })
      .catch(error => console.error('Error fetching data:', error));
  }


  // Fetch and populate data for ECB Marginal Lending Facility
  fetchDataAndPopulate('api/get_ECB_MLF/', 'dataTableMLF', 'dataChartMLF', 'Marginal Lending Facility Rate');

  // Fetch and populate data for ECB Deposit Facility
  fetchDataAndPopulate('api/get_ECB_DF/', 'dataTable', 'dataChart', 'Deposit Facility Rate');

  fetchDataAndPopulate('api/get_ECB_MRO/', 'dataTableMRO', 'dataChartMRO', 'Main refinancing operations - fixed rate tenders');
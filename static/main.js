// Fetch attendance every 2 seconds
function fetchAttendance() {
    fetch('/attendance')
        .then(response => response.json())
        .then(data => {
            let tbody = document.querySelector("#attendanceTable tbody");
            tbody.innerHTML = "";
            data.forEach(item => {
                let row = `<tr><td>${item.name}</td><td>${item.time}</td></tr>`;
                tbody.innerHTML += row;
            });
        });
}

setInterval(fetchAttendance, 2000);

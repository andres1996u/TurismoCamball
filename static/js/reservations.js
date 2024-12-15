fetch('/my_reservations')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById('reservations-list');
    list.innerHTML = data.map(res => `
      <div>
        <h3>Reserva para ${res.destination_id}</h3>
        <p>Fecha: ${res.date}</p>
        <p>Personas: ${res.people}</p>
        <button onclick="cancelReservation('${res._id}')">Cancelar</button>
      </div>
    `).join('');
  })
  .catch(error => console.error('Error:', error));

function cancelReservation(id) {
  fetch(`/cancel_reservation/${id}`, { method: 'DELETE' })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

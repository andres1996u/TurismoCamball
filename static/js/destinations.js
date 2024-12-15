document.getElementById('filter-btn').addEventListener('click', () => {
    const region = document.getElementById('region').value;
    const priceRange = document.getElementById('price-range').value;
  
    fetch(`/destinations?region=${region}&price_range=${priceRange}`)
      .then(response => response.json())
      .then(data => {
        const list = document.getElementById('destinations-list');
        list.innerHTML = data.map(dest => `
          <div>
            <h3>${dest.name}</h3>
            <p>${dest.description}</p>
            <p>Precio: COP ${dest.price}</p>
          </div>
        `).join('');
      })
      .catch(error => console.error('Error:', error));
  });
  
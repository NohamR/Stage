fetch('result.txt')
  .then(response => response.text())
  .then(data => {
    const imageLinks = data.split('\n');
    const container = document.getElementById('imageContainer');

    imageLinks.forEach(link => {
      if (link.trim() !== '') {
        const img = document.createElement('img');
        img.src = link;
        img.style.display = 'block';
        container.appendChild(img);
      }
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });

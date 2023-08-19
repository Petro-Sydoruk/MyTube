chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === 'downloadMusic') {
    const url = request.url;
    const output_path = 'C:/Users/p3--/Music/MyTube';  // Змініть цей шлях на вірний

    fetch('http://localhost:5000/download', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: url, output_path: output_path })
    })
    .then(response => response.json())
    .then(data => {
      sendResponse({ success: true, message: data.message });
    })
    .catch(error => {
      sendResponse({ success: false, message: error.message });
    });

    return true;  // Повертаємо true для асинхронної відповіді
  }
});


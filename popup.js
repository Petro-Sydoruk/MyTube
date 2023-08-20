document.addEventListener('DOMContentLoaded', function() {
  const downloadButton = document.getElementById('downloadButton');

  downloadButton.addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      const activeTab = tabs[0];
      const url = activeTab.url;

      chrome.runtime.sendMessage({ action: 'downloadMusic', url: url }, function(response) {
        if (response.success) {
          console.log('Downloaded successfully:', response.message);
        } else {
          console.error('Error:', response.message);
        }
      });
    });
  });
});

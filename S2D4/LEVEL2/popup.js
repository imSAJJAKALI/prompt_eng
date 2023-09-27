// Add a click event listener to the button
document.getElementById('changeColorButton').addEventListener('click', changeBackgroundColor);

// Function to change the background color of the current tab
function changeBackgroundColor() {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    // You can customize the color here, e.g., 'red', 'blue', '#FFA500' (orange)
    var newColor = '#FFA500';
    
    // Send a message to the content script to change the background color
    chrome.tabs.sendMessage(tabs[0].id, { action: 'changeColor', color: newColor });
  });
}

// Listen for messages from the popup
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
    if (message.action === 'changeColor') {
      // Change the background color of the page
      document.body.style.backgroundColor = message.color;
    }
  });
  
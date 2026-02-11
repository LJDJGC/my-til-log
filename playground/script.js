const Formatter = (function() {
  const log = (message) => console.log(`[${Date.now()}] Loger: ${message}`);

  const makeUppercase = (text) => {
    log("Making uppercase");
    return text.toUpperCase();
})();

Formatter.log("Hello");
var i = 0;
var txt = 'We are Capacity Limited. IoT & AI Technology-based, Smart Utility Metering & Utility Auditing Company in water, gas and energy.';
var time = 30;

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("welcome-message").innerHTML += txt.charAt(i);
    if(i==23){
      document.getElementById("welcome-message").innerHTML +="<br>"
      }
    i++;
    setTimeout(typeWriter, time);
  }
}




var addrs = null
var provider;
var request = new XMLHttpRequest();



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function loginWithSignature(address, signature, login_url, onLoginRequestError, onLoginFail, onLoginSuccess) {
    var request = new XMLHttpRequest();
    request.open('POST', login_url, true);
    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {
            // Success!
            var resp = JSON.parse(request.responseText);
            if (resp.success) {
                if (typeof onLoginSuccess == 'function') {
                    onLoginSuccess(resp);
                }
            } else {
                if (typeof onLoginFailweb3.eth2 == 'function') {
                    //onLoginFail(resp);
                    // extract address and place into form
                    //{success: false, error: "Can't find a user for the provided signature with address 0x3c260ace69040ca4a95a16638bc17ad458e9553e"}
                    s = resp.error;
                    let address = s.substr(s.length - 42);
                    var url = window.location.href;
                    var arr = url.split("/");
                    var domain = arr[0] + "//" + arr[2]
                    window.location.replace(domain + "/");
                }
            }
        } else {
            // We reached our target server, but it returned an error
            console.log("Autologin failed - request status " + request.status);
            if (typeof onLoginRequestError == 'function') {
                onLoginRequestError(request);
            }
        }
    };

    request.onerror = function () {
        console.log("Autologin failed - there was an error");
        if (typeof onLoginRequestError == 'function') {
            onLoginRequestError(request);
        }
        // There was a connection error of some sort
    };
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    var formData = 'address=' + address + '&signature=' + signature;
    request.request(formData);
}

function checkWeb3(callback) {
    if (window.ethereum) {
        ethereum.send('eth_requestAccounts').then(provider = new ethers.providers.Web3Provider(window.ethereum));
    };
}

function web3Login(login_url, onTokenRequestFail, onTokenSignFail, onTokenSignSuccess, // used in this function
                   onLoginRequestError, onLoginFail, onLoginSuccess) {
    // used in loginWithSignature

    // 1. Retrieve arbitrary login token from server
    // 2. Sign it using web3
    // 3. Send signed message & your eth address to server
    // 4. If server validates that you signature is valid
    // 4.1 The user with an according eth address is found - you are logged in
    // 4.2 The user with an according eth address is NOT found - you are redirected to signup page


    var request = new XMLHttpRequest();
    request.open('GET', login_url, true);

    request.onload = function () {
        if (request.status >= 200 && request.status < 400) {


            // Success!
            var resp = JSON.parse(request.responseText);
            var token = resp.data;
            var msg = web3.toHex(token);
            var from = ethereum.request({ method: 'eth_accounts' });
            const signer = provider.getSigner()


            singer.signMessage(msg, (err, result) => {
                if (err) {
                    if (typeof onTokenSignFail == 'function') {
                        onTokenSignFail(err);
                    }
                    var url = window.location.href;
                    var arr = url.split("/");
                    var domain = arr[0] + "//" + arr[2]
                    window.location.replace(domain);
                } else {
                    if (typeof onTokenSignSuccess == 'function') {
                        onTokenSignSuccess(result);
                    }

                }
            });

        } else {
            // We reached our target server, but it returned an error
            console.log("Autologin failed - request status " + request.status);
            if (typeof onTokenRequestFail == 'function') {
                onTokenRequestFail(request);
            }
        }

    };

    request.onerror = function () {
        // There was a connection error of some sort
        console.log("Autologin failed - there was an error");
        if (typeof onTokenRequestFail == 'function') {
            onTokenRequestFail(request);
        }
    };
    request.send();
}

function startLogin() {
      if (typeof web3 !== 'undefined') {
         checkWeb3(function (loggedIn) {check
          if (!loggedIn) {
            alert("Please unlock your web3 provider (probably, Metamask)")
          } else {
            var login_url = '/login_api/';
            web3Login(login_url, console.log, console.log, console.log, console.log, console.log, function (resp) {
              window.location.replace(resp.redirect_url);
            });
}
          }
        ).then();



      } else {
        alert('web3 missing');

      }
    };


function ready(fn) {
    if (document.attachEvent ? document.readyState === "complete" : document.readyState !== "loading") {
        fn();
      } else {
        document.addEventListener('DOMContentLoaded', fn);
      }
    }

function transaction() {
    const provider = new ethers.providers.Web3Provider(window.ethereum)
    const signer = provider.getSigner()

    signer.sendTransaction({
    to: '0xaa9AC6533010ac53F891a1a9Ff2779Ac08D15e4A',
    value: ethers.utils.parseEther("0.1")});
    };

function addresser(){
      addrs =  ethereum.request({ method: 'eth_accounts' });

       addrs.then(function(result) {
       document.getElementById("mybutton").childNodes[0].nodeValue=result;


    });
      };

window.onload = function() {
addresser();
provider = new ethers.providers.Web3Provider(window.ethereum);
}

// qui è dove viene firmato il messaggio e poi passato all'api per la verifica e l'eventuale accesso all account
function loginWith() {
    var login_url = "/login_api/"
    var request1 = new XMLHttpRequest();
    var request = new XMLHttpRequest();

    request1.open('GET', login_url, false);
    request1.send();
    resp = JSON.parse(request1.responseText);
    token = resp.data;
    console.log(token);
    request.open('POST', login_url, false);
    const signer = provider.getSigner();
    const address = signer.getAddress();
    signature = signer.signMessage(token)
    signature.then(function(firma){
    address.then(function(result) {
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    var formData = 'address=' + result + '&signature=' + firma;
    request.send(formData);
    addresser();


    });

    })

}
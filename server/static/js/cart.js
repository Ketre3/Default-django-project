"use strict"

// Get it from django tutorial
const getCookie = name => {
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let cookie of cookies) {
          cookie = cookie.trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              return decodeURIComponent(cookie.substring(name.length + 1));
          }
      }
  }
  return null;
 }

const api = async function(url, method, body=null) {
  let response;
  if (method === "GET" || method === "HEAD") {
    response = await fetch(url, {
        "method": method,
        "headers": {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie('csrftoken'),
        },
    });
  } else {
    response = await fetch(url, {
        "method": method,
        "body": JSON.stringify(body),
        "headers": {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie('csrftoken'),
        },
    });
  }
  const data = await response.json();
  return data;
}

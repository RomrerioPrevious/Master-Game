const url  = "http://localhost:5500/graphql";

const makeRequest = (query) => {
    return fetch(url, {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify({ query })
    }).then((res) => res.json());
}
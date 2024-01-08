function addToCart(id, name, price) {
    fetch('/api/cart', {
        method: "post",
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price
        }),
        headers: {
            'Content-Type': "application/json"
        }
    }).then(function(res) {
        return res.json();
    }).then(function(data) {
        let c = document.getElementsByClassName('cart-counter');
        for (let d of c)
            d.innerText = data.total_quantity
    })
}

//function pay() {
//    if (confirm("Bạn chắc chắn thanh toán!") === true) {
//        fetch("/api/employee/pay", {
//            method: "post"
//        }).then(res => res.json()).then(data => {
//            if (data.status === 200)
//                location.reload();
//            else
//                alert(data.err_msg);
//        })
//
//    }
//}

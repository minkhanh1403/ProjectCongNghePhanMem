function addComment(productId) {
    if (confirm("Bạn chắc chắn bình luận?") == true) {
        fetch(`/api/products/${productId}/comments`, {
            method: "post",
            body: JSON.stringify({
                "content": document.getElementById("comment").value
            }),
            headers: {
                'Content-Type': "application/json"
            }
        }).then(res => res.json()).then(data => {
            if (data.status === 200) {
                let d = document.getElementById("comments");
                let c = data.c;
                d.innerHTML = `
                 <div class="row alert alert-info">
                    <div class="col-md-1">
                        <img src="${c.user.avatar}" class="img-fluid rounded" />
                    </div>
                    <div class="col-md-11">
                        <p>${ c.content }</p>
                        <p>Bình luân lúc: <span class="my-date">${  moment(c.created_date).locale("vi").fromNow() }</span></p>
                    </div>
                </div>
                `  + d.innerHTML;
            }
        })
    }
}



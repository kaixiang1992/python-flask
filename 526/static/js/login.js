window.onload = function () {
    document.getElementsByClassName('submitbutton')[0].onclick = function (event) {
        event.preventDefault();
        let params = new FormData();
        params.append('email', document.querySelectorAll('input[name="email"]')[0].value);
        params.append('psd', document.querySelectorAll('input[name="psd"]')[0].value);
        axios.post('http://127.0.0.1:5000/login/', params, { headers: { 'X-CSRFToken': document.querySelectorAll('meta[name="csrf-token"]')[0].content}}).then(res => {
            console.log(res);
            const  { data, status } = res;
            if(status == 200){
                alert(data);
            }else{
                alert(data);
            }
        }).catch(err => {
            console.log(err);
        });
    }
}
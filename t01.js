function submit(){
    $.ajax({
        url:"",
        type:"post",
        dataType:"json",
        data:JSON.stringify({
                Number:   $("#Num").val(),
            }),
        success:function (data){
            console.log("传送成功")
            console.log(data)
            console.log(data.status)
            console.log(data.time)
        },
        error:function (){
            alert("传送失败")
        }
    })
}
function reset(){
    document.getElementById("myForm").reset()
}
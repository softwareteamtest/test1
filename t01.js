function submit(){
    $.ajax({
        url:"",
        type:"post",
        dataType:"text",
        data:{
<<<<<<< HEAD
                Number: $("#Num").val(),
=======
                Number:   $("#Num").val(),
>>>>>>> f2cda898105b5403d388be429dba3b4830568bce
            },
        success:function (data){
            console.log("传送成功")
            console.log(data)
            console.log(data.status)
            console.log(data.time)
<<<<<<< HEAD
            alert(data)
=======
            alert(date)
>>>>>>> f2cda898105b5403d388be429dba3b4830568bce
        },
        error:function (){
            alert("传送失败")
        }
    })
}
function reset(){
    document.getElementById("myForm").reset()
}
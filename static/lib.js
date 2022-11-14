
function sendException(){
    base=document.getElementById('base')
    lista=document.getElementById('lista')
    if (base.value.length >= 2 && lista.value.length>0){
        let postObj = { 
            base: base.value,
            list: lista.value.split("\n")
        }
        console.log(postObj)
        fetch("/api/view", {
            method: 'post',
            body: JSON.stringify(postObj),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            return response.json()
        }).then((res) => {
            const success = addNotification(NOTIFICATION_TYPES.SUCCESS, base.value+' saved!');
        }).catch((error) => {
            console.log(error)
            const errorNotification = addNotification(NOTIFICATION_TYPES.DANGER, 'error saving '+base.value+', see console log');
        })
    }
}

function deleteException(base){
    elem=encodeURIComponent(base)
    fetch("/api/delete/"+elem, {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json()
    }).then((res) => {
        el=document.getElementById('exc_'+base.replace(' ','_'))
        console.log(el)
        el.parentNode.removeChild(el);
        const notif = addNotification(NOTIFICATION_TYPES.SUCCESS, base+' succesfully removed');
    }).catch((error) => {
        console.log(error)
        const errorNotification = addNotification(NOTIFICATION_TYPES.DANGER, 'error deleting '+base+', see console log');
    })
}

function publishException(){
    fetch("/api/publish", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json()
    }).then((res) => {
        //window.location.href="/";
        document.getElementById('publishAlert').innerHTML='<a><span class="material-symbols-sharp">done_all</span></a>';
        const notif = addNotification(NOTIFICATION_TYPES.SUCCESS, 'Exception published!');
    }).catch((error) => {
        console.log(error)
        const errorNotification = addNotification(NOTIFICATION_TYPES.DANGER, 'error publishing Exceptions');
    })
}


function isPublished(){
    fetch("/api/published", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json()
    }).then((res) => {
        if (res){
            document.getElementById('publishAlert').innerHTML='<a><span class="material-symbols-sharp">done_all</span></a>';
        }
        else{
            document.getElementById('publishAlert').innerHTML='<a><span class="material-symbols-sharp alertColor">warning</span></a>';
        }
    }).catch((error) => {
        console.log(error)
    })
}

function searchException(){
    searchFor=document.getElementById('searchFor')
    pattern=document.getElementById('searchPattern')

    if (searchFor.value.length >= 2 
        && pattern.value.length>0){
        let postObj = { 
            for: searchFor.value,
            pattern: pattern.value
        }
        console.log(postObj)
        fetch("/api/search", {
            method: 'post',
            body: JSON.stringify(postObj),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            return response.json()
        }).then((res) => {
            if (res['ok']!==undefined && res['ok']=='ko'){
                const errorNotification = addNotification(NOTIFICATION_TYPES.DANGER, res['msg']);
            }
            else{
                console.log(res)
                lista=document.getElementById('lista')
                stringa=res.join("\n")
                console.log(stringa)
                lista.value=stringa
            }
        }).catch((error) => {
            console.log(error)
        })
    }    

}


function reloadException(){
    fetch("/api/reload", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        return response.json()
    }).then((res) => {
        if (res){
            document.location.href="/";
        }
        else{
            const errorNotification = addNotification(NOTIFICATION_TYPES.DANGER, 'Reload Errors');
        }
    }).catch((error) => {
        console.log(error)
    })

}

isPublished()
setInterval(isPublished, 5000);

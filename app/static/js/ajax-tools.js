export function sendAjax(url, method='get', data = null)
{
    return new Promise((resolve, reject) =>
    {
        const request =  new XMLHttpRequest();

        request.addEventListener('readystatechange', (e) =>
        {
            if(request.readyState === 4)
            {
                const data = request.responseText

                if(/^2[0-9]{2}$/.test(request.status))
                {
                    resolve(data);
                } else
                {
                    reject(data);
                }
            }
        });

        request.open(method, url, true);
        request.send(data);
    })
}
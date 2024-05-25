(function(win,doc){
    'use script';

    if(doc.querySelector('#formCard')){
        let formCard = doc.querySelector('#formCard');
        formCard.addEventListener('submit',(e)=>{
            e.preventDefault();
            let card = PagSeguro.encryptCard({
                publicKey: doc.querySelector('#publicKey').value,
                holder: doc.querySelector('#cardHolder').value,
                number: doc.querySelector('#cardNumber').value,
                expMonth: doc.querySelector('#cardMonth').value,
                expYear: doc.querySelector('#cardYear').value,
                securityCode: doc.querySelector('#cardCvv').value
            });
            let encrypted = card.encryptedCard;
            doc.querySelector('#encriptedCard').value = encrypted;
            formCard.submit();
        });
    }
})(window,document);
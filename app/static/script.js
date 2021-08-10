const vgsForm = window.VGSCollect.create('tntr4uij4qf', 'SANDBOX', () => {});

const css = {
  boxSizing: 'border-box',
  fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI"',
};

vgsForm.field('#cc-number', {
  type: 'card-number',
  name: 'card_number',
  successColor: '#4F8A10',
  errorColor: '#D8000C',
  placeholder: 'Card number',
  showCardIcon: true,
  validations: ['required', 'validCardNumber'],
  css: css,
});

vgsForm.field('#cc-cvc', {
  type: 'card-security-code',
  name: 'card_cvc',
  successColor: '#4F8A10',
  errorColor: '#D8000C',
  placeholder: 'CVC',
  maxLength: 3,
  validations: ['required', 'validCardSecurityCode'],
  css: css,
});

vgsForm.field('#cc-expiration-date', {
  type: 'card-expiration-date',
  name: 'card_exp',
  successColor: '#4F8A10',
  errorColor: '#D8000C',
  placeholder: 'MM / YY',
  validations: ['required', 'validCardExpirationDate'],
  css: css,
});

document.getElementById("collect-form").addEventListener('submit', (e) => {
  e.preventDefault();
  vgsForm.submit('/post', {}, (status, response) => {
    if (status === 200) {
      console.log("response");
    }
  }, (error) => {
    console.log(error);
  });
});



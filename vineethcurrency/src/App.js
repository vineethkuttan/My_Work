import React,{useEffect,useState} from 'react';
import './App.css';
import CurrencyRow  from './CurrencyRow';

const BASE_URL ='https://api.exchangeratesapi.io/latest'
function App() {
  const [currencyOptions,setCurrencyOptions]=useState([])
  const [FromCurrency,setFromCurrency]=useState()
  const [ToCurrency, setToCurrency] = useState()
  const [exchangeRate, setExchangeRate]=useState()
  const [amount,setAmount]=useState(1)
  const [amountInFromCurrency, setAmountInFromCurrency]=useState(true)
  console.log(currencyOptions)

  let toAmount,fromAmount
  if(amountInFromCurrency)
  {
    fromAmount=amount
    toAmount=amount*exchangeRate
  }
  else{
    toAmount=amount
    fromAmount=amount/exchangeRate
  }

  useEffect(()=>{
    fetch(BASE_URL)
      .then(res=>res.json())
      .then(data=>
      {
        const firstCurrency=Object.keys(data.rates)[0]
        setCurrencyOptions([data.base,...Object.keys(data.rates)])
        setFromCurrency(data.base)
        setToCurrency(firstCurrency)
        setExchangeRate(data.rates[firstCurrency])
      })

  },[])

  useEffect(()=>{
    if(FromCurrency !=null && ToCurrency!=null)
    fetch(`${BASE_URL}?base=${FromCurrency}&symbols=${ToCurrency}`)
      .then(res=>res.json())
      .then(data=>setExchangeRate(data.rates[ToCurrency]))
  },[FromCurrency,ToCurrency])

  function handleFromAmountChange(e) {
      setAmount(e.target.value)
      setAmountInFromCurrency(true)
  }
  function handleToAmountChange(e) {
    setAmount(e.target.value)
    setAmountInFromCurrency(false)
  }
 const onChangeCurrencyT= event => setToCurrency(event.target.value)
 const onChangeCurrencyF = event => setFromCurrency(event.target.value)
  return (
    <>
    <h1>Vineeth Currency Converter</h1>
      <CurrencyRow currencyOptions={currencyOptions} onChangeAmount={handleFromAmountChange} amount={fromAmount} selectCurrency={FromCurrency} onChangeCurrency={onChangeCurrencyF}/>
    <div className="equals">=</div>
      <CurrencyRow currencyOptions={currencyOptions} onChangeAmount={handleToAmountChange} amount={toAmount} selectCurrency={ToCurrency} onChangeCurrency={onChangeCurrencyT}/>
    </>
  );
}

export default App;

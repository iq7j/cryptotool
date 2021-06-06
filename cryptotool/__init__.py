
class crypto:
	def find(coin,c1,c2):
		    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+coin+'&tsyms='+c1+','+c2+'')
		    r = r.json()
		    usd = r[c1]
		    eur = r[c2]
		    print("yout first coin compared to",coin,"is",usd)
		    print("you second coin compared to",coin,"is",eur)

import pandas as pd
import pandas_datareader as pddr
import requests
import json

# =============================================================================
# 'annualOtherCurrentAssets', 
# 'annualCapitalStock', 
# 'annualCashAndCashEquivalents', 
# 'annualAccountsReceivable', 
# 'annualAccountsPayable', 
# 'annualLongTermDebt', 
# 'annualStockholdersEquity', 
# 'annualOtherNonCurrentLiabilities', 
# 'annualTotalNonCurrentLiabilitiesNetMinorityInterest', 
# 'annualOtherCurrentLiabilities', 
# 'annualCurrentDebt', 
# 'annualInvestmentsAndAdvances', 
# 'annualNonCurrentDeferredTaxesLiabilities', 
# 'annualTotalLiabilitiesNetMinorityInterest', 'annualOtherShortTermInvestments', 
# 'annualIncomeTaxPayable', 
# 'annualCashCashEquivalentsAndShortTermInvestments', 
# 'annualGoodwill', 
# 'annualTotalAssets', 
# 'annualOtherIntangibleAssets', 
# 'annualRetainedEarnings', 
# 'annualCurrentAccruedExpenses', 
# 'annualInventory', 
# 'annualNonCurrentDeferredRevenue', 
# 'annualAccumulatedDepreciation', 
# 'annualCurrentLiabilities', 
# 'annualNetPPE', 
# 'annualGrossPPE', 
# 'annualTotalNonCurrentAssets', 
# 'annualOtherNonCurrentAssets', 
# 'annualCurrentAssets', 
# 'annualCurrentDeferredRevenue', 
# 'annualGainsLossesNotAffectingRetainedEarnings'
# =============================================================================

def request_financials(ticker='AAPL', periods_ago='0'):

    yahoo_url = 'https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{ticker}?lang=en-US&region=US&symbol={ticker}&padTimeSeries=true&type=annualTotalAssets%2CtrailingTotalAssets%2CannualStockholdersEquity%2CtrailingStockholdersEquity%2CannualGainsLossesNotAffectingRetainedEarnings%2CtrailingGainsLossesNotAffectingRetainedEarnings%2CannualRetainedEarnings%2CtrailingRetainedEarnings%2CannualCapitalStock%2CtrailingCapitalStock%2CannualTotalLiabilitiesNetMinorityInterest%2CtrailingTotalLiabilitiesNetMinorityInterest%2CannualTotalNonCurrentLiabilitiesNetMinorityInterest%2CtrailingTotalNonCurrentLiabilitiesNetMinorityInterest%2CannualOtherNonCurrentLiabilities%2CtrailingOtherNonCurrentLiabilities%2CannualNonCurrentDeferredRevenue%2CtrailingNonCurrentDeferredRevenue%2CannualNonCurrentDeferredTaxesLiabilities%2CtrailingNonCurrentDeferredTaxesLiabilities%2CannualLongTermDebt%2CtrailingLongTermDebt%2CannualCurrentLiabilities%2CtrailingCurrentLiabilities%2CannualOtherCurrentLiabilities%2CtrailingOtherCurrentLiabilities%2CannualCurrentDeferredRevenue%2CtrailingCurrentDeferredRevenue%2CannualCurrentAccruedExpenses%2CtrailingCurrentAccruedExpenses%2CannualIncomeTaxPayable%2CtrailingIncomeTaxPayable%2CannualAccountsPayable%2CtrailingAccountsPayable%2CannualCurrentDebt%2CtrailingCurrentDebt%2CannualTotalNonCurrentAssets%2CtrailingTotalNonCurrentAssets%2CannualOtherNonCurrentAssets%2CtrailingOtherNonCurrentAssets%2CannualOtherIntangibleAssets%2CtrailingOtherIntangibleAssets%2CannualGoodwill%2CtrailingGoodwill%2CannualInvestmentsAndAdvances%2CtrailingInvestmentsAndAdvances%2CannualNetPPE%2CtrailingNetPPE%2CannualAccumulatedDepreciation%2CtrailingAccumulatedDepreciation%2CannualGrossPPE%2CtrailingGrossPPE%2CannualCurrentAssets%2CtrailingCurrentAssets%2CannualOtherCurrentAssets%2CtrailingOtherCurrentAssets%2CannualInventory%2CtrailingInventory%2CannualAccountsReceivable%2CtrailingAccountsReceivable%2CannualCashCashEquivalentsAndShortTermInvestments%2CtrailingCashCashEquivalentsAndShortTermInvestments%2CannualOtherShortTermInvestments%2CtrailingOtherShortTermInvestments%2CannualCashAndCashEquivalents%2CtrailingCashAndCashEquivalents&merge=false&period1=493590046&period2=1597872911&corsDomain=finance.yahoo.com'
    yahoo_url = yahoo_url.format(ticker=ticker)

    response = requests.get(yahoo_url)
    response = response.json()
    response = response['timeseries']['result']

    attribute_dictionary = {}
    for item in range(len(response)):
        #Get attribute name.
        attribute_name = response[item]['meta']['type'][0]
        #Clean attribute data.
        if attribute_name in response[item]:
            attribute_data = response[item][attribute_name]
            attribute_data = attribute_data[len(attribute_data)-1-periods_ago]
        #Set attribute name and data.
        attribute_dictionary.update({attribute_name:attribute_data})
        # print(attribute_name)
        # print(attribute_data)
        # print("\n")

    return attribute_dictionary

# def get_financial_data(ticker='AAPL'):

financials = request_financials('MSFT', 1)

financials_df = pd.DataFrame(financials['annualCurrentLiabilities'])

print(financials_df)



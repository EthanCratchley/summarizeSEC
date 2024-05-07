from openai import OpenAI
import os

def summarize_article(sec_filing):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("No OPENAI_API_KEY set for the environment")

    client = OpenAI(api_key=openai_api_key)
    prompt = f"Summarize the provided SEC Filing: {sec_filing}\nInclude key information such as Net Income, Cash, Debt, Shares Outstanding, and anything else important."
    
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1000
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in summarization: {e}"

sec = '''
Apple Inc.
CONDENSED CONSOLIDATED STATEMENTS OF OPERATIONS (Unaudited)
(In millions, except number of shares, which are reflected in thousands, and per-share amounts)

Three Months Ended		Six Months Ended
March 30,
2024		April 1,
2023		March 30,
2024		April 1,
2023
Net sales:							
   Products	$	66,886 			$	73,929 			$	163,344 			$	170,317 	
   Services	23,867 			20,907 			46,984 			41,673 	
Total net sales	90,753 			94,836 			210,328 			211,990 	
Cost of sales:							
   Products	42,424 			46,795 			100,864 			107,560 	
   Services	6,058 			6,065 			12,338 			12,122 	
Total cost of sales	48,482 			52,860 			113,202 			119,682 	
Gross margin	42,271 			41,976 			97,126 			92,308 	
Operating expenses:							
Research and development	7,903 			7,457 			15,599 			15,166 	
Selling, general and administrative	6,468 			6,201 			13,254 			12,808 	
Total operating expenses	14,371 			13,658 			28,853 			27,974 	
Operating income	27,900 			28,318 			68,273 			64,334 	
Other income/(expense), net	158 			64 			108 			(329)	
Income before provision for income taxes	28,058 			28,382 			68,381 			64,005 	
Provision for income taxes	4,422 			4,222 			10,829 			9,847 	
Net income	$	23,636 			$	24,160 			$	57,552 			$	54,158 	
Earnings per share:							
Basic	$	1.53 			$	1.53 			$	3.72 			$	3.42 	
Diluted	$	1.53 			$	1.52 			$	3.71 			$	3.41 	
Shares used in computing earnings per share:							
Basic	15,405,856 			15,787,154 			15,457,810 			15,839,939 	
Diluted	15,464,709 			15,847,050 			15,520,675 			15,901,384 	
 
See accompanying Notes to Condensed Consolidated Financial Statements.
Apple Inc. | Q2 2024 Form 10-Q | 1

Apple Inc.
CONDENSED CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME (Unaudited)
(In millions)

Three Months Ended		Six Months Ended
March 30,
2024		April 1,
2023		March 30,
2024		April 1,
2023
Net income	$	23,636 			$	24,160 			$	57,552 			$	54,158 	
Other comprehensive income/(loss):							
Change in foreign currency translation, net of tax	(322)			(95)			(14)			(109)	
Change in unrealized gains/losses on derivative instruments, net of tax:							
Change in fair value of derivative instruments	456 			(13)			(75)			(1,001)	
Adjustment for net (gains)/losses realized and included in net income	232 			(191)			(591)			(1,957)	
Total change in unrealized gains/losses on derivative instruments	688 			(204)			(666)			(2,958)	
Change in unrealized gains/losses on marketable debt securities, net of tax:							
Change in fair value of marketable debt securities	(7)			1,403 			3,038 			2,303 	
Adjustment for net (gains)/losses realized and included in net income	59 			62 			134 			127 	
Total change in unrealized gains/losses on marketable debt securities	52 			1,465 			3,172 			2,430 	
Total other comprehensive income/(loss)	418 			1,166 			2,492 			(637)	
Total comprehensive income	$	24,054 			$	25,326 			$	60,044 			$	53,521 	
 
See accompanying Notes to Condensed Consolidated Financial Statements.
Apple Inc. | Q2 2024 Form 10-Q | 2

Apple Inc.
CONDENSED CONSOLIDATED BALANCE SHEETS (Unaudited)
(In millions, except number of shares, which are reflected in thousands, and par value)

March 30,
2024		September 30,
2023
ASSETS:
Current assets:			
Cash and cash equivalents	$	32,695 			$	29,965 	
Marketable securities	34,455 			31,590 	
Accounts receivable, net	21,837 			29,508 	
Vendor non-trade receivables	19,313 			31,477 	
Inventories	6,232 			6,331 	
Other current assets	13,884 			14,695 	
Total current assets	128,416 			143,566 	
Non-current assets:			
Marketable securities	95,187 			100,544 	
Property, plant and equipment, net	43,546 			43,715 	
Other non-current assets	70,262 			64,758 	
Total non-current assets	208,995 			209,017 	
Total assets	$	337,411 			$	352,583 	
LIABILITIES AND SHAREHOLDERS’ EQUITY:
Current liabilities:			
Accounts payable	$	45,753 			$	62,611 	
Other current liabilities	57,298 			58,829 	
Deferred revenue	8,012 			8,061 	
Commercial paper	1,997 			5,985 	
Term debt	10,762 			9,822 	
Total current liabilities	123,822 			145,308 	
Non-current liabilities:			
Term debt	91,831 			95,281 	
Other non-current liabilities	47,564 			49,848 	
Total non-current liabilities	139,395 			145,129 	
Total liabilities	263,217 			290,437 	
Commitments and contingencies			
Shareholders’ equity:			
Common stock and additional paid-in capital, $0.00001 par value: 50,400,000 shares authorized; 15,337,686 and 15,550,061 shares issued and outstanding, respectively
78,815 			73,812 	
Retained earnings/(Accumulated deficit)	4,339 			(214)	
Accumulated other comprehensive loss	(8,960)			(11,452)	
Total shareholders’ equity	74,194 			62,146 	
Total liabilities and shareholders’ equity	$	337,411 			$	352,583 	
 
See accompanying Notes to Condensed Consolidated Financial Statements.
Apple Inc. | Q2 2024 Form 10-Q | 3

Apple Inc.
CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS (Unaudited)
(In millions)

Six Months Ended
March 30,
2024		April 1,
2023
Cash, cash equivalents and restricted cash, beginning balances
$	30,737 			$	24,977 	
Operating activities:			
Net income	57,552 			54,158 	
Adjustments to reconcile net income to cash generated by operating activities:			
Depreciation and amortization	5,684 			5,814 	
Share-based compensation expense	5,961 			5,591 	
Other	(1,971)			(1,732)	
Changes in operating assets and liabilities:			
Accounts receivable, net	7,727 			9,596 	
Vendor non-trade receivables	12,164 			14,785 	
Inventories	53 			(2,548)	
Other current and non-current assets	(4,438)			(4,092)	
Accounts payable	(16,710)			(20,764)	
Other current and non-current liabilities	(3,437)			1,757 	
Cash generated by operating activities	62,585 			62,565 	
Investing activities:			
Purchases of marketable securities	(25,042)			(11,197)	
Proceeds from maturities of marketable securities	27,462 			17,124 	
Proceeds from sales of marketable securities	4,314 			1,897 	
Payments for acquisition of property, plant and equipment	(4,388)			(6,703)	
Other	(729)			(247)	
Cash generated by investing activities	1,617 			874 	
Financing activities:			
Payments for taxes related to net share settlement of equity awards	(2,875)			(2,734)	
Payments for dividends and dividend equivalents	(7,535)			(7,418)	
Repurchases of common stock	(43,344)			(39,069)	
Repayments of term debt	(3,150)			(3,651)	
Repayments of commercial paper, net	(3,982)			(7,960)	
Other	(132)			(455)	
Cash used in financing activities	(61,018)			(61,287)	
Increase in cash, cash equivalents and restricted cash	3,184 			2,152 	
Cash, cash equivalents and restricted cash, ending balances
$	33,921 			$	27,129 	
Supplemental cash flow disclosure:			
Cash paid for income taxes, net	$	14,531 			$	4,894 	
 
'''
print(summarize_article(sec))

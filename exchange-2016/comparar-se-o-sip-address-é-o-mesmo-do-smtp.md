# Comparar se o SIP address é o mesmo do SMTP

Date: 2016-10-04 18:59:51

Categories: Exchange 2010, Exchange 2013, Exchange 2016, Office 365

---

<p>Em uma nova demanda tive que identificar se os endereços SIP dos usuários eram os mesmos do SMTP para que todos estejam corretos antes da migração para o Office 365. Que tal um script simples e funcional que exporte esses dados?</p>
<blockquote>
<pre>[String] $strPrimaryAddress
[String] $strSIP
[Array] $arrCollection = @()

$servers = @("SERVER1","SERVER2","SERVER3")
foreach($server in $servers){

ForEach ($mbx in (Get-Mailbox -server $server -ResultSize Unlimited))
{
 # Initialize object to hold all the information
 $mbcomb = "" | Select "Display Name", "Primary SMTP Address", "SIP"
 
 # Reset variables
 $strPrimaryAddress = $strSIP = $NULL
 
 # Check all the e-mail aliases the user has
 $mbx.EmailAddresses | ForEach {
 If ($_.IsPrimaryAddress -and $_.Prefix -match "SMTP") { $strPrimaryAddress = $_.SmtpAddress }
 If ($_.PrefixString -eq "sip") { $strSIP = $_.AddressString }
 }
 
 # Compare the primary SMTP with the SIP address
 If ($strPrimaryAddress -ne $strSIP)
 {
 $mbcomb."Display Name" = $mbx.DisplayName
 $mbcomb."Primary SMTP Address" = $strPrimaryAddress
 $mbcomb."SIP" = $strSIP
 
 $arrCollection += $mbcomb
 }
}
}
# Print or export all the results
#$arrCollection | FT
$arrCollection | Export-Csv .\"SMTPvsSIP_$(Get-Date -f 'yyyyMMdd').csv" -NoType</pre>
</blockquote>
<p>Esqueci de comentar que no meu ambiente existem servidores em vários lugares pelo mundo, por isso a exportação precisava indicar os servers.</p>
<p>Fonte: <a href="http://www.msexchange.org/kbase/ExchangeServerTips/ExchangeServer2010/Powershell/ComparePrimarySMTPaddresswithSIPaddress.html">Aqui</a></p>

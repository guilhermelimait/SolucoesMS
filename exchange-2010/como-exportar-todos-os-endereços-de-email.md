# Como exportar todos os endereços de email?

Date: 2013-12-06 13:00:46

Categories: Exchange 2010

---

<p>Para exportar todos os endereços de email existentes em sua organização, basta utilizar da seguinte linha de comando:</p>
<blockquote>
<pre>Get-Mailbox -resultsize 9999| Select Name, @{Name=’EmailAddresses’;Expression={[string]::join(",", ($_.EmailAddresses))}} | Export-CSV c:EmailAddress_mailbox.csv</pre>
</blockquote>
<p>Caso precise aumentar o número de saídas (+9999) altere apenas o número 9999 no comando para &#8220;<em>Unlimited</em>&#8221;</p>
<p>Abaixo mais dois exemplos para exportar os conatatos e as distribuição:</p>
<blockquote>
<pre>Get-contact -resultsize 9999| Select Name, @{Name=’EmailAddresses’;Expression={[string]::join(",", ($_.EmailAddresses))}} | Export-CSV c:EmailAddress_contact.csv
 Get-distributiongroup -resultsize 9999 | Select Name, @{Name=’EmailAddresses’;Expression={[string]::join(",", ($_.EmailAddresses))}} | Export-CSV c:EmailAddress_DL.csv</pre>
</blockquote>
<p>Enjoy!</p>

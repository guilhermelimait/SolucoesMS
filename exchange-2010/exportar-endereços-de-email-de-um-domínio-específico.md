# Exportar endereços de email de um domínio específico

Date: 2017-10-10 14:25:03

Categories: Exchange 2010

---

<p>Precisa exportar usuários com um endereço de domínio específico na sua estrutura? Que tal exportar utilizando um comando simples?</p>
<blockquote>
<pre>Get-CASMailbox -ResultSize unlimited | where {$_.primarysmtpaddress -like "*@dominioespecifico.com.br"} | select displayname, primarysmtpaddress| export-csv .\ExportUsers.csv</pre>
</blockquote>
<p>Enjoy!</p>

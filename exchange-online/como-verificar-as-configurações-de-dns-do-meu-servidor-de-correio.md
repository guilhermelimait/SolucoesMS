# Como verificar as configurações de DNS do meu servidor de correio?

Date: 2020-04-16 11:45:35

Categories: Comando local/PC, Exchange, Exchange 2010, Exchange 2013, Exchange 2016, Exchange 2019, Exchange Online, Gerenciamento, O365, Office 365, Powershell

---

<p>Olá pessoal,<br />
Caso, após a migração do seu servidor de correio queira verificar se as configurações de DNS ficaram corretas, é possível utilizar dos comandos abaixo:</p>
<p>Resolve-DnsName -Type A -Name mail.domain.com<br />
Resolve-DnsName -Type A -Name autodiscover.domain.com<br />
Resolve-DnsName -Type A -Name mail.domain.com -Server 8.8.8.8<br />
Resolve-DnsName -Type A -Name autodiscover.domain.com -Server 8.8.8.8<br />
Resolve-DnsName -Type MX -Name domain.com -Server 8.8.8.8<br />
Resolve-DnsName -Type TXT -Name domain.com -Server 8.8.8.8<br />
Resolve-DnsName -Type A -Name i-should-not-exist.domain.com -Server 8.8.8.8</p>
<p>Enjoy!</p>

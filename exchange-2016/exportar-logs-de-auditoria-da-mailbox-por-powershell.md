# Exportar Logs de Auditoria da Mailbox por Powershell

Date: 2019-02-12 14:05:18

Categories: Exchange, Exchange 2016, Office 365

---

<p>Hi all!</p>
<p>Para exportar informações sobre a caixa de correio de um usuário é preciso verificar se, a auditoria foi habilitada para o usuário e se ele possui licenciamento E3 pelo menos. Para isso, execute os seguintes comandos:</p>
<pre><span style="color: #ff0000;">Get-Mailbox usuario@dominio.com.br | select *audit*</span></pre>
<p>Caso o resultado tenha o auditenabled como true, exporte os dados usando o seguinte comando e informando o período que quer analisar, no caso abaixo estamos usando 1000 horas como exemplo.</p>
<pre><span style="color: #ff0000;">Search-MailboxAuditLog usuario@dominio.com.br -StartDate (get-date).addhours(-1000) -ShowDetails | export-csv .\export-usuario.csv -Delimiter ";"</span></pre>
<p>Também pode ser feito com uma data de referência, recomendo utilizar por até 30 dias devido o log ser meio louco na exportação.</p>
<pre><span style="color: #ff0000;">Search-MailboxAuditLog usuario@dominio.com.br -StartDate 2019/01/31 -EndDate 2019/02/11 -ShowDetails | export-csv .\export-usuario.csv -Delimiter ";"</span></pre>
<p>Enjoy!</p>

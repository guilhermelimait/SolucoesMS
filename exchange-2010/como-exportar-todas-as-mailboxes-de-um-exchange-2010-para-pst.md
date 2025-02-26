# Como exportar todas as mailboxes de um Exchange 2010 para .pst?

Date: 2020-03-16 11:40:42

Categories: Exchange, Exchange 2010

---

<p>Mais uma tarefa simpleas mas cheia de descobertas e atividades por aqui. Um cliente precisa exportar todos seus dados de um exchange 2010 antigo para PST para fim de arquivo. Para isso, existem várias formas de executá-lo, porém, é preciso fazer algumas atividades antes, vamos conferir?</p>
<h4>01 &#8211; Permissão para exportar os dados:</h4>
<p>Crie as permissões para que seu usuário possa exportar os dados de dentro do Exchange para uma pasta compartilhada, dê essas permissões ao seu usuário de admin, marcado em vermelho.</p>
<pre class="brush: powershell; title: ; notranslate" title="">New-ManagementRoleAssignment –Role &quot;Mailbox Import Export&quot; –User Administrator </pre>
<h4>02 &#8211; Permissão no compartilhamento para receber os arquivos:</h4>
<p>Crie uma nova pasta que irá receber os dados exportados, compartilhe a pasta e adicione as permissões (no compartilhamento e na guia segurança) abaixo:</p>
<ul>
<li>Full Access : EXCHANGE TRUSTED SUBSYSTEM (grupo)</li>
<li>Full Access: Domains Admins</li>
</ul>
<h4>03 &#8211; Exporte a lista de usuários que gostaria de exportar dados para um pst:</h4>
<p>Utilize do código abaixo no seu Microsoft Exchange Powershell para exportar as informações:</p>
<pre class="brush: powershell; title: ; notranslate" title="">Get-Mailbox -resultsize unlimited| select displayname, primarysmtpaddress | export-csv .\mailbox.csv -NoTypeInformation -Encoding unicode</pre>
<h4>04 &#8211; Use o código abaixo para exportar os dados para a pasta que você indicar:</h4>
<p>Salve o código abaixo em um arquivo chamado ExportMailboxData.ps1 com o seguinte conteúdo:</p>
<pre class="brush: powershell; title: ; notranslate" title="">
write-host
Clear-Host
$desc = @&quot;
  DEVELOPED BY : Guilherme Lima
  PLATFORM     : Exchange 2010
  WEBSITE      : http://solucoesms.com.br
  WEBSITE2     : http://github.com/guilhermelimait
  LINKEDIN     : https://www.linkedin.com/in/guilhermelimait/
  DESCRIPTION  : Export users mailbox data from the local server to a UNC path
&quot;@
Write-host $desc -ForegroundColor darkgreen
Write-Host
$UNCpath = &quot;\\servidor\pastacompartilhada&quot;
$Batch = &quot;lote01&quot;
get-mailboxexportrequest -batchname $Batch | REMOVE-mailboxexportrequest
$Users = get-content .\Mailbox.txt
foreach($user in $users){
    $DName = get-mailbox $user | select-object -expandproperty displayname
    New-MailboxExportRequest $user -FilePath &quot;$UNCpath\$DName.pst&quot; -batchname $Batch
    write-host &quot; &gt; Export Process of user: $DName.pst was initiated&quot; -foreground darkyellow
</pre>
<h4>05 &#8211; Acompanhe a Exportação:</h4>
<p>Você deve ter percebido que existe uma variável chamada $batch, insira nela o valor do lote que você quer pesquisar, dessa forma, poderá fazer vários lotes separadamente e sempre que precisar saber como vai o processo de exportação e se foi concluído com sucesso, execute o comando informando o nome do lote que você executou no passo anterior:</p>
<pre class="brush: powershell; title: ; notranslate" title="">get-mailboxexportrequest -batchname lote01 </pre>
<h4>06 &#8211; Fim!</h4>
<p>O que acharam? Bem simples não é mesmo?</p>

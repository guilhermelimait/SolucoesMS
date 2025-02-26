# Como exportar Mailbox para um PST com o Exchange Server 2010?

Date: 2013-07-11 16:00:33

Categories: Exchange, Exchange 2010

---

<p>Olá pessoal, seguindo nossa linha de conhecimentos gerais sobre gerenciamento e controle dos serviços de Exchange eis que surge mais uma dúvida, como posso exportar uma mailbox para um PST? como? COMO???<br />
Sim é possível fazer no Exchange 2010 SP1 sem a complicação do Exchange 2007, que tinha que ter uma console x86 com outlook na mesma máquina e isso nem sempre era possível.<br />
No Exchange 2007 você tinha que criar muita confusão pra exportar apenas um cliente, agora no Exchange 2010 SP1 você precisa apenas solicitar uma requisição de exportação/migração e o Exchange cuida de tudo, ao final o cliente migrado terá um icone de exportado/migrado.</p>
<p>Para iniciar é preciso que você tenha o direito de &#8220;Mailbox Import Export&#8221;, essa regra existe mas não está habilitada para todos, é preciso ativá-la. Outro ponto, é que o Exchage não vai exportar para um caminho local, apenas para caminhos UNC, ou seja, apenas para caminhos de rede.</p>
<p>Vamos começar? Abra o Exchange Management Shell e ative a regra para seu usuário admin:</p>
<blockquote>
<pre>[PS] C:&gt;New-ManagementRoleAssignment –Role "Mailbox Import Export" –User Administrator</pre>
</blockquote>
<p>Saia do console e abra novamente para que possa conseguir continuar com os direitos.</p>
<p>Para exportar uma conta siga o seguinte comando:</p>
<blockquote>
<pre>[PS] C:&gt;New-MailboxExportRequest -Mailbox GUILHERME.LIMA -FilePath \EXServer01pstGUILHERME.LIMA.pst</pre>
</blockquote>
<p>Que tal descobrir como está o status de migração? Faça o seguinte:</p>
<blockquote>
<pre>[PS] C:&gt;Get-MailboxExportRequest -Name MailboxExport | fl</pre>
</blockquote>
<p>Se tiver mais usuários com a exportação, é possível ver todos os status de uma só vez:</p>
<blockquote>
<pre>[PS] C:&gt;Get-MailboxExportRequest | Get-MailboxExportRequestStatistics</pre>
</blockquote>
<p>Já que você já fez a exportação dos dados e já monitorou o processo, é hora de limpar a solicitação de exportação, para isso faça o seguinte comando:</p>
<blockquote>
<pre>[PS] C:&gt;Get-MailboxExportRequest | where {$_.status -eq "Completed"} | Remove-MailboxExportRequest</pre>
</blockquote>
<p>Enjoy!</p>

# Importar módulo do Exchange no VSCode usando MFA

Date: 2019-10-11 11:04:50

Categories: DevOps, Exchange, Gerenciamento, MFA, O365, Powershell, VSCode

---

<p><img loading="lazy" decoding="async" class="aligncenter wp-image-898 size-large" src="http://solucoesms.com.br/wp-content/uploads/2019/10/ambiente-desenvolvimento-javascript-1024x576.png" alt="" width="678" height="381" srcset="https://solucoesms.com.br/wp-content/uploads/2019/10/ambiente-desenvolvimento-javascript-1024x576.png 1024w, https://solucoesms.com.br/wp-content/uploads/2019/10/ambiente-desenvolvimento-javascript-300x169.png 300w, https://solucoesms.com.br/wp-content/uploads/2019/10/ambiente-desenvolvimento-javascript-768x432.png 768w, https://solucoesms.com.br/wp-content/uploads/2019/10/ambiente-desenvolvimento-javascript.png 1140w" sizes="auto, (max-width: 678px) 100vw, 678px" /></p>
<p style="text-align: justify;">Olá pessoal! Novamente venho aqui e compartilhar uma dica para quem é de <em>DEVOPS</em> e gosta de usar o VSCode pra manter versionamento de código, conexão com O365 e execução de atividades em lote no Exchange.</p>
<p style="text-align: justify;">Se você conseguiu se identificar com o que comentei, sabe que a Microsoft nos permite fazer dois tipos de conexão no O365, uma por autenticação padrão, e outra com um módulo de MFA (Multi Factor Authentication). O problema é que ao se conectar ao Exchange para fazer conexões de Powershell usando o MFA ficamos reféns do shell da própria Microsoft.</p>
<p style="text-align: justify;">Abaixo vamos usar um script chamado MFAAuthentication.ps1 para se conectar ao módulo de Exchange no O365 e explicarei linha-à-linha o que estamos executando. Vamos entender o que está acontecendo?</p>
<p><strong>Comando completo:</strong></p>
<div>
<div>
<pre>Import-Module $((Get-ChildItem -Path $($env:LOCALAPPDATA+"\Apps\2.0\") -Filter Microsoft.Exchange.Management.ExoPowershellModule.dll -Recurse ).FullName|where-object{$_ -notmatch "_none_"}|Select-Object -First 1)
$EXOSession = New-ExoPSSession
Import-PSSession $EXOSession</pre>
</div>
</div>
<p><strong>Explicação:</strong></p>
<p style="text-align: justify;">Primeiramente, vamos importar o módulo do exchange no caminho padrão após sua instalação pelo método explicado na fonte 2 desse artigo.</p>
<pre>Import-Module $((Get-ChildItem -Path $($env:LOCALAPPDATA+"\Apps\2.0\") -Filter Microsoft.Exchange.Management.ExoPowershellModule.dll -Recurse ).FullName|where-object{$_ -notmatch "_none_"}|Select-Object -First 1)</pre>
<p style="text-align: justify;">Iniciamos uma nova conexão no O365 onde o usuário e senha serão verificados além do MFA via telefone ou pela forma que foi configurada por você no momento da primeira habilitação.</p>
<pre>$EXOSession = New-ExoPSSession</pre>
<p>Após a validação, importamos a variável com a validação e passamos a conectar à uma nova sessão no O365.</p>
<pre>Import-PSSession $EXOSession</pre>
<p><strong>Conclusão:</strong></p>
<p>Pronto! Você já pode utilizar dos seus scripts ou comandos para gerenciar seu ambiente de Exchange via O365 pelo Visual Studio Code!</p>
<p>Se tiverem dúvidas sobre o VSCode com Powershell e se quiserem saber um pouco mais, posso continuar compartilhando alguns posts por aqui, o que acham?</p>
<p><strong>Fonte:</strong></p>
<p>MFA: https://docs.microsoft.com/pt-br/office365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide</p>
<p>MFA Exchange: https://docs.microsoft.com/pt-br/powershell/exchange/exchange-online/connect-to-exchange-online-powershell/mfa-connect-to-exchange-online-powershell?view=exchange-ps</p>
<p>&nbsp;</p>

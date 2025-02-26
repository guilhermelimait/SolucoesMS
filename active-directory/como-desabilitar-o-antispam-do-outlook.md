# Como desabilitar o antispam do Outlook

Date: 2017-06-22 17:57:15

Categories: Active Directory

---

<p style="text-align: justify;">O cliente me pediu para desabilitar o antispam do Outlook para evitar que mensagens sejam direcionadas para a pasta de Spam já que a maioria é enviada por sistemas antigos.</p>
<p style="text-align: justify;">Para desabilitar os filtros, vá até a seguinte chave no registro e adicione a chave <strong>DisableAntiSpam</strong> do tipo <strong>DWORD</strong>. Salve com o valor 1, se não existir a chave, por favor, crie-a.</p>
<p style="text-align: center;"><em><strong>Observação: Valor 1 desabilita e o valor 0 habilita</strong></em></p>
<p>No Outlook 2016, abra o registro e vá até o caminho abaixo:</p>
<pre>HKEY_CURRENT_USER\Software\Policies\Microsoft\office\16.0\outlook
DWORD: DisableAntiSpam</pre>
<p>No Outlook 2013, abra o registro e vá até o caminho abaixo:</p>
<pre>HKEY_CURRENT_USER\Software\Policies\Microsoft\office\15.0\outlook
DWORD: DisableAntiSpam</pre>
<p>No Outlook 2010, abra o registro e vá até o caminho abaixo:</p>
<pre>HKEY_CURRENT_USER\Software\Policies\Microsoft\office\14.0\outlook</pre>
<p>No Outlook 2007, abra o registro e vá até o caminho abaixo:</p>
<pre>HKEY_CURRENT_USER\Software\Policies\Microsoft\office\12.0\outlook</pre>

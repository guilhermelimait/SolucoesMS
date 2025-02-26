# Como criar Impersonate para um usuário?

Date: 2014-08-14 13:58:40

Categories: Exchange 2007, Exchange 2010

---

<p>O Impersonate ou Impersonation é uma propriedade que pode ser adicionada a uma conta de correio para que o usuário final possa fazer pesquisas em outras caixas sem necessitar de autenticação. Geralmente é aplicada à uma conta de serviço e ajuda muito em algumas situações.</p>
<p>Abaixo estão duas soluções, ambas aplicadas para a mesma conta de correio porém uma solução indicada para o Exchange 2007 e outra para o Exchange 2010.</p>
<p>Exchange 2007:</p>
<pre>Get-ExchangeServer | where {$_.IsClientAccessServer -eq $TRUE} | ForEach-Object {Add-ADPermission -Identity $_.distinguishedname -User (Get-User -Identity USERMBX | select-object).identity -AccessRights GenericAll -InheritanceType Descendents}
Get-ExchangeServer | where {$_.IsClientAccessServer -eq $TRUE} | ForEach-Object {Add-ADPermission -Identity $_.distinguishedname -User (Get-User -Identity USERMBX | select-object).identity -extendedRight ms-Exch-EPI-Impersonation}</pre>
<p>Exchange 2010:</p>
<pre>New-ManagementRoleAssignment –Name:USERMBXApplicationImpersonation –Role:ApplicationImpersonation –User:USERMBX</pre>
<p>Enjoy!</p>
<p>&nbsp;</p>

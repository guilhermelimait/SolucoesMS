# Adicionar usuários à uma sala de reunião restrita

Date: 2018-06-26 19:19:58

Categories: Office 365

---



Nesse caso, preciso adicionar um novo usuário para a sala restrita sem perder nenhum dos que já possuem esse acesso. Para isso, um script simples pode ser usado:
<pre>function Add-CalendarBookInPolicy {
Param(
$RoomName
, $newDelegate
)
$BookInPolicy = (Get-CalendarProcessing -Identity $RoomName).BookInPolicy
$BookInPolicy += $newDelegate
Set-CalendarProcessing -Identity $RoomName -BookInPolicy $BookInPolicy
}
Add-CalendarBookInPolicy -Identity $Roomname "saladereuniao@dominio.com.br" -newDelegate "usuario@dominio.com.br"</pre>







<p class="wp-block-verse">Ainda é possível fazer uma alteração para que adicionem os responsáveis pra aprovação nas reuniões, para isso utilize o seguinte código:</p>

<pre>function Add-CalendarResourceDelegate {
Param(
$RoomName
, $newDelegate
)
$resourceDelegates = (Get-CalendarProcessing -Identity $RoomName).ResourceDelegates
$resourceDelegates += $newDelegate
Set-CalendarProcessing -Identity $RoomName -ResourceDelegates $resourceDelegates
}
Add-CalendarResourceDelegate -Identity $Roomname "saladereuniao@dominio.com.br" -newDelegate "usuario@dominio.com.br"</pre>
<strong><span style="color: #ff0000;">Update:</span></strong>

Existe também uma forma mais simples de configurar tudo usando apenas uma linha de comando:
<pre>Set-CalendarProcessing -Identity recurso@dominio.com.br -AutomateProcessing AutoAccept -BookInPolicy "user1@dominio.com","user2@dominio.com" -AllBookInPolicy $false
</pre>
<strong>Fonte:</strong> <a href="https://docs.microsoft.com/en-us/powershell/module/exchange/mailboxes/Set-CalendarProcessing?view=exchange-ps">https://docs.microsoft.com/en-us/powershell/module/exchange/mailboxes/Set-CalendarProcessing?view=exchange-ps</a>

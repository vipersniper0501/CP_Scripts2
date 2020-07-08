
function crtgrup { #create group
    Clear-Host
    $crtgruyn = Read-Host -Prompt 'Do you want to create a new local user group? [y/n] '
    if ($crtgruyn -eq 'y'){
        $crtgru = $True
        while ($crtgru -eq $True){
            $ngrunm = Read-Host -Prompt 'What is the name of the new group? '
            New-LocalGroup -Name $ngrunm
            Write-Output("New group " + $ngrunm + " has been created!")

            $anotgru = Read-Host -Prompt 'Would you like to make another local user group? [y/n] '
            if ($anotgru -eq 'y'){
                return $True0
            } else {
                return $crtgru = $False
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function rusrfgru { #remove user from group
    Clear-Host
    Write-Output("")
    Get-LocalGroup
    Write-Output("")
    $rgrusrf = Read-Host -Prompt 'Would you like to remove a user from a group? [y/n] '
    if ($rgrusrf -eq 'y'){
        $agn = $true
        while ($agn -eq $true){
            Clear-Host
            Write-Output("")
            $usrnam = Read-Host -Prompt 'What is the name of the user you would like to remove from a group? '
            $gru = Read-Host -Prompt 'What is the name of the group you would like the user removed from? '
            Remove-LocalGroupMember -Group $gru -Member $usrnam -Confirm
            Write-Output("User " + $usrnam + " has been removed from group " + $gru + "!")
            $agnyn = Read-Host -Prompt 'Would you like to remove another user from another local user group? [y/n] '
            if ($agnyn -eq 'y'){
                return $agn = $true
            } else {
                return $agn = $false
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function auts { #Add user to system
    Clear-Host
    $augruyn = Read-Host -Prompt 'Would you like to add a user to the system? [y/n]'
    if ($augruyn -eq 'y'){
        $augag = $true
        while ($augag -eq $true){
            $admn = Read-Host -Prompt 'Will the user be an admin? [y/n] '
            if ($admn -eq 'y'){
                $nusnm = Read-Host -Prompt 'What would you like the name of the user to be? '
                $nuspss = Read-Host -Prompt -AsSecureString 'Please input a new password for the user '
                New-LocalUser $nusnm -Password $nuspss -Confirm
                Add-LocalGroupMember -Group "Administrators" -Member $nusnm
                Get-LocalUser
            } else {
                $nusnm = Read-Host -Prompt 'What would you like the name of the user to be? '
                $nuspss = Read-Host -Prompt -AsSecureString 'Please input a new password for the user '
                New-LocalUser $nusnm -Password $nuspss -Confirm
                Get-LocalUser
            }
            $augagyn = Read-Host -Prompt 'Would you like to add another user to the system? [y/n] '
            if ($augagyn -eq 'y'){
                return $augag = $true
            } else {
                return $augag = $false
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function rusr { #Remove user
    Clear-Host
    Write-Output("")
    $rusyn = Read-Host -Prompt 'Would you like to remove a user from this system? [y/n] '
    if ($rusyn -eq 'y'){
	    $remvusr = $True
	    while ($remvusr -eq $True){
            Get-LocalUser
            $rus = Read-Host -Prompt 'Which user would you like to remove from the system? '
            Remove-LocalUser -Name $rus -Confirm
            Write-Output("User " + $rus + " has been removed!")
            Write-Output("")
            $remvanthusr = Read-Host -Prompt 'Would you like to remove another user? [y/n] '
            if ($remvanthusr -eq 'y')
            {
                $remvusr = $True
            }
            else
            {
                $remvusr = $False
            }
        } else {
	    Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
       }
    }
}

function rusrgru { #remove group from system
    Clear-Host
    Write-Output("")
    Get-LocalGroup
    Write-Output("")
    $rusrgruyn = Read-Host -Prompt 'Would you like to remove a Local User Group from this list of groups on the system? [y/n] '
    if ($rusrgruyn -eq 'y'){
        $rgru = $true
        while ($rgru -eq $true){
            Clear-Host
            Get-LocalGroup
            Write-Output("")
            $grunam = Read-Host -Prompt 'Which group would you like to remove from this system?'
            Remove-LocalGroup -Name $grunam -Confirm
            Write-Output("The local group " + $grunam + " has been removed!")
            Write-Output("")
            $end = Read-Host -Prompt 'Would you like to remove another group from the list? [y/n] '
            if ($end -eq 'y')
            {
                return $rgru = $true
            }
            else
            {
                return $rgru = $false
            }
        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

function autgru { #Add user to group
    Clear-Host
    Write-Output("")
    $autgruyn = Read-Host -Prompt 'Would you like to add a user to a group? [y/n] '
    if ($autgruyn -eq 'y'){
        $autgruag = $true
        while ($autgruag -eq $true){
            Get-LocalUser
            Clear-Host #This is done so it is a gurantee that the list will show
            Get-LocalUser
            $usrnam = Read-Host -Prompt 'What user would you like to add to a group? '
            Get-LocalGroup
            Clear-Host #This is done so it is a gurantee that the list will show
            Get-LocalGroup
            $usrgruadd = Read-Host -Prompt 'Which local group would you like to add' + $usrnam + ' to? '
            Add-LocalGroupMember -Name $usrnam -Member $usrgruadd
            Write-Output("User " + $usrnam + " has been add to group " + $usrgruadd + "! ")
            $autag = Read-Host -Prompt 'Would you like to add another user to another group? [y/n] '
            if ($autag -eq 'y'){
                return $autgruag = $true
            } else {
                return $autgruag = $false
            }

        }
    } else {
        Read-Host -Prompt 'Press any key to continue... '
        usr_grumnu
    }
}

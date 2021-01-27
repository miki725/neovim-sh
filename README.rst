neovim.sh
=========

Wrapper package to install `neovim` with an executable.

This allows to install `neovim` with `pipx`:

.. code:: bash

    pipx install --python=$(which python2) neovim-sh
    pipx install --python=$(which python3) neovim-sh

To use in `neovim`, simply set python host program variables:

.. code:: vim

    function! s:SetPythonHostProg(job_id, data, event)
        if (len(a:data[0]) > 0)
            execute(a:data[0])
        endif
    endfunction

    " jobstart is only in neovim
    if exists("*jobstart")
        let _ = jobstart(['neovim2.sh', '--vim'], {'on_stdout': function('s:SetPythonHostProg')})
        let _ = jobstart(['neovim3.sh', '--vim'], {'on_stdout': function('s:SetPythonHostProg')})
    endif

# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>${project}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <style type="text/css">
      .switch {
        font-size: 1rem;
        position: relative;
      }
      .switch input {
        position: absolute;
        height: 1px;
        width: 1px;
        background: none;
        border: 0;
        clip: rect(0 0 0 0);
        clip-path: inset(50%);
        overflow: hidden;
        padding: 0;
      }
      .switch input + label {
        position: relative;
        min-width: calc(calc(2.375rem * .8) * 2);
        border-radius: calc(2.375rem * .8);
        height: calc(2.375rem * .8);
        line-height: calc(2.375rem * .8);
        display: inline-block;
        cursor: pointer;
        outline: none;
        user-select: none;
        vertical-align: middle;
        text-indent: calc(calc(calc(2.375rem * .8) * 2) + .5rem);
      }
      .switch input + label::before,
      .switch input + label::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: calc(calc(2.375rem * .8) * 2);
        bottom: 0;
        display: block;
      }
      .switch input + label::before {
        right: 0;
        background-color: #dee2e6;
        border-radius: calc(2.375rem * .8);
        transition: 0.2s all;
      }
      .switch input + label::after {
        top: 2px;
        left: 2px;
        width: calc(calc(2.375rem * .8) - calc(2px * 2));
        height: calc(calc(2.375rem * .8) - calc(2px * 2));
        border-radius: 50%;
        background-color: white;
        transition: 0.2s all;
      }
      .switch input:checked + label::before {
        background-color: #08d;
      }
      .switch input:checked + label::after {
        margin-left: calc(2.375rem * .8);
      }
      .switch input:focus + label::before {
        outline: none;
        box-shadow: 0 0 0 0.2rem rgba(0, 136, 221, 0.25);
      }
      .switch input:disabled + label {
        color: #868e96;
        cursor: not-allowed;
      }
      .switch input:disabled + label::before {
        background-color: #e9ecef;
      }
      .switch.switch-sm {
        font-size: 0.875rem;
      }
      .switch.switch-sm input + label {
        min-width: calc(calc(1.9375rem * .8) * 2);
        height: calc(1.9375rem * .8);
        line-height: calc(1.9375rem * .8);
        text-indent: calc(calc(calc(1.9375rem * .8) * 2) + .5rem);
      }
      .switch.switch-sm input + label::before {
        width: calc(calc(1.9375rem * .8) * 2);
      }
      .switch.switch-sm input + label::after {
        width: calc(calc(1.9375rem * .8) - calc(2px * 2));
        height: calc(calc(1.9375rem * .8) - calc(2px * 2));
      }
      .switch.switch-sm input:checked + label::after {
        margin-left: calc(1.9375rem * .8);
      }
      .switch.switch-lg {
        font-size: 1.25rem;
      }
      .switch.switch-lg input + label {
        min-width: calc(calc(3rem * .8) * 2);
        height: calc(3rem * .8);
        line-height: calc(3rem * .8);
        text-indent: calc(calc(calc(3rem * .8) * 2) + .5rem);
      }
      .switch.switch-lg input + label::before {
        width: calc(calc(3rem * .8) * 2);
      }
      .switch.switch-lg input + label::after {
        width: calc(calc(3rem * .8) - calc(2px * 2));
        height: calc(calc(3rem * .8) - calc(2px * 2));
      }
      .switch.switch-lg input:checked + label::after {
        margin-left: calc(3rem * .8);
      }
      .switch + .switch {
        margin-left: 1rem;
      }
    </style>
  </head>
  <body>
	<br>
	  <div class=container>

      <div class="col-12 col-lg-6 offset-lg-3">
        <div class="card mb-4">
          <div class="card-header">
            <h3>Select sites to block</h3>
          </div>

          <form action="save" method="POST" class="form-horizontal" id="block-form">
            <div class="card-body">
              % for item in servers:
                <div class="form-group form-row">
                  <div class="col-1 col-sm-1 pt-2">
                    % if 'icon' in servers[item]:
                      <img src="${servers[item]['icon']}" alt="${item}" class="img-fluid"/>
                    % else:
                      <img src="https://www.${servers[item]['domains'][0]}/apple-touch-icon-precomposed.png" alt="${item}" class="img-fluid img-fallback" data-site="${item}" data-favicon="https://www.${servers[item]['domains'][0]}/favicon.ico"/>
                    % endif
                  </div>
                  <div class="col-8 col-sm-9">
                    <div class="lead">
                      ${item}
                    </div>
                    <small id="${item}HelpBlock" class="form-text text-muted">
                      ${", ".join(servers[item]['domains'])}
                    </small>
                  </div>
                  <div class="col-3 col-sm-2 pt-2">
                    <span class="switch">
                      <input class="switch" data-toggle="toggle" ${'checked' if servers[item]['blocked'] else ''} type="checkbox" id="${item}" name="${item}" data-onstyle="danger" aria-describedby="${item}HelpBlock">
                      <label for="${item}"></label>
                    </span>
                  </div>
                </div>
              % endfor
            </div>
          </form>
        </div>
      </div>
	  </div>


    <script src="https://code.jquery.com/jquery-3.3.1.min.js" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>

    <script type="text/javascript">
      $('.img-fallback').on('error', function() {
        var text = $(this).data('site');
        var faviconUrl = $(this).data('favicon');
        var placeholderUrl = 'https://via.placeholder.com/250/ffffffff/00000000?text=' + text;

        if (this.src != faviconUrl && this.src != placeholderUrl) {
          this.src = faviconUrl;
        } else if (this.src == faviconUrl) {
          this.src = placeholderUrl;
        }
      });
    </script>

    <script type="text/javascript">
      $(document).ready(function() {
        $('#block-form input[type="checkbox"]').change(function() {
          $.post('save', $('#block-form').serialize());
        });
      });
    </script>
  </body>
</html>

// custom javascript

$( document ).ready(() => {
  console.log('Sanity Check!');
});

$('.btn').on('click', function() {
  _file_type = $('#filebtn').val()
  _model_name = $('#modelbtn').val()
  _uri = $('#uri').val()
  $.ajax({
    url: '/task',
    data: { 
      file_type: _file_type,
      model_name: _model_name,
      url: _uri
    },
    method: 'GET',
    dataType: 'JSON'
  })
  .done((res) => {
    getStatus(res.data.task_id)
  })
  .fail((err) => {
    console.log(err)
  });
});

function getStatus(taskID) {
  $.ajax({
    url: `/tasks/${taskID}`,
    method: 'GET'
  })
  .done((res) => {
    const html = `
      <tr>
        <td>${res.data.task_id}</td>
        <td>${res.data.task_status}</td>
        <td>${res.data.task_result}</td>
        <td>${res.data.message}</td>
      </tr>`
    $('#tasks').prepend(html);
    const taskStatus = res.data.task_status;
    if (taskStatus === 'finished' || taskStatus === 'failed') return false;
    setTimeout(function() {
      getStatus(res.data.task_id);
    }, 1000);
  })
  .fail((err) => {
    console.log(err)
  });
}
